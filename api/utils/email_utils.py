from fastapi_mail import FastMail, MessageSchema, MessageType
from api.configs.email_config import conf
from typing import Optional

async def send_email(subject: str, recipients: list[str], template_name: str,  context: Optional[dict] = None):
    from main import email_templates
    from premailer import transform

    message = MessageSchema(
        subject=subject,
        recipients=recipients,
        subtype=MessageType.html
    )

    # Render the template with context
    html = email_templates.get_template(template_name).render(context)
    message.body = transform(html)

    try:
        fm = FastMail(conf)
        await fm.send_message(message)
    except Exception as e:
        print(e)