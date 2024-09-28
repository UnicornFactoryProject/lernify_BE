from fastapi_mail import FastMail, MessageSchema, MessageType, ConnectionConfig
from typing import Optional
from premailer import transform
from app.configs import config

conf = ConnectionConfig(
    MAIL_USERNAME = config.MAIL_USERNAME,
    MAIL_PASSWORD = config.MAIL_PASSWORD,
    MAIL_FROM = config.MAIL_FROM,
    MAIL_FROM_NAME = config.MAIL_FROM_NAME,
    MAIL_SERVER = config.MAIL_SERVER,
    MAIL_PORT = config.MAIL_PORT,
    MAIL_TLS = config.MAIL_TLS,
    MAIL_SSL = config.MAIL_SSL,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

async def send_email(subject: str, recipient: str, template_name: str,  context: Optional[dict] = None):
    from main import email_templates
    
    # Ensure recipients are in list format
    message = MessageSchema(
        subject=subject,
        recipients=[recipient],
        subtype=MessageType.html
    )
    
    if context is None:
        context = {}

    # Render the template with context
    html = email_templates.get_template(template_name).render(context)
    message.body = transform(html)

    try:
        fm = FastMail(conf)
        await fm.send_message(message)
        print(f"Email sent successfully to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")