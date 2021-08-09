from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question
from ..models import User


def detail_profile(request, author_id):
	user = User.objects.get(id=author_id)
	context = {'user': user}
	return render(request, 'pybo/profile.html', context)
