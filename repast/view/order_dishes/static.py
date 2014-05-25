# coding: utf-8
from flask import render_template, request


def pay1():
    return render_template("reception/pay1.html")


def pay2():
    return render_template("reception/pay2.html")


def pay3():
    return render_template("reception/pay3.html")


def pay4():
    return render_template("reception/pay4.html")


def pay5():
    return render_template("reception/pay5.html")


def myTel():
    return render_template("reception/mytel.html")


def my():
    return render_template("reception/my.html")
