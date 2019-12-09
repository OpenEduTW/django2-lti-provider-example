from django.shortcuts import render
from django.views.generic.base import TemplateView
from lti_provider.mixins import LTIAuthMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.context_processors import csrf
import logging

logger = logging.getLogger('debug')


def index(request):
    return render(request, "main/index.html", locals())


class LTIAssignment1View(LTIAuthMixin, LoginRequiredMixin, TemplateView):
    template_name = 'main/assignment.html'

    def get_context_data(self, **kwargs):
        return {
            'is_student': self.lti.lis_result_sourcedid(self.request),
            'course_title': self.lti.course_title(self.request),
            'number': 1,
        }
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update(csrf(request))
        return render(request,self.template_name,context=context)