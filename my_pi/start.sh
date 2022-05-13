#!/bin/bash
gunicorn -k eventlet -w 1 --reload app:app