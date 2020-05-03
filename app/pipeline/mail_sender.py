#!/usr/bin/env python

import smtplib
from autocurry import autocurry


@autocurry
def sendmail(recipients, text):
    SERVER = "server"
    FROM = "greg@gbell.bitwombat.com.au"
    SUBJECT = "New Local Stories"

    email = """\
From: %s
To: %s
Subject: %s

%s
""" % (
        FROM,
        ", ".join(recipients),
        SUBJECT,
        text,
    )

    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, recipients, email)
    server.quit()
