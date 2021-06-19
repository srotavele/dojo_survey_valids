from flask import Flask, render_template, request, redirect, session
from flask_app import app
from ..models.display_mdl import Display
from ..models.login_mdl import Login