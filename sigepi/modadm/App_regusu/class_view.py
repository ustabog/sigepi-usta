from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .models import *
from .form import *
