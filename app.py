#!/usr/bin/env python3
import os

import aws_cdk as cdk

from staticwebsite.staticwebsite_stack import StaticwebsiteStack

app = cdk.App()
StaticwebsiteStack(app, "StaticWebsiteStack")

app.synth()
