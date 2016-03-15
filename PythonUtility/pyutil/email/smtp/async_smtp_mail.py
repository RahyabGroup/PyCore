import asyncio
import functools
from pyutil.email.smtp.smtp_mail import SmtpMail

__author__ = 'H.Rouhani'


class AsyncSmtpMail(SmtpMail):
    @asyncio.coroutine
    def send(self, sender, receivers, subject, content, message_type="plain"):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().send, sender, receivers, subject, content, message_type))
        yield from fut
