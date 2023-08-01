from django.views.generic import TemplateView
from .models import Challenge, ChallengeCategory


class ChallengeCategoryListView(TemplateView):
    model = Challenge
    
    template_name = 'challenges/challenges_category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = ChallengeCategory.objects.all()

        context['categories'] = categories

        return context
    


class ChallengeListView(TemplateView):
    model = Challenge

    template_name = 'challenges/challenges_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = self.kwargs['category']

        context['challenges'] = Challenge.objects.filter(category__name=category)

        context['category'] = ChallengeCategory.objects.get(name=category)

        return context



class ChallengeDetailsView(TemplateView):
    model = Challenge

    template_name = 'challenges/view_challenge.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        challenge_uuid = self.kwargs['challenge_uuid']

        context["challenge"] = Challenge.objects.get(uuid=challenge_uuid)

        return context
    
    
    