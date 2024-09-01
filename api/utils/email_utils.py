from fastapi_mail import FastMail, MessageSchema, MessageType
from api.configs.email_config import conf
from typing import Optional

async def send_email(subject: str, recipients: list[str], template_name: str,  context: Optional[dict] = None):
    from main import email_templates
    from premailer import transform
    retry = 2

    message = MessageSchema(
        subject=subject,
        recipients=recipients,
        subtype=MessageType.html
    )

    # Render the template with context
    html = email_templates.get_template(template_name).render(context)
    message.body = transform(html)

    for i in range(retry):
        try:
            fm = FastMail(conf)
            await fm.send_message(message)
            print("Email sent successfully")
            break
        except Exception as e:
            print(e)