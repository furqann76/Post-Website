"""import openai
from django.core.management.base import BaseCommand
from blog.models import Post
from django.conf import settings


class Command(BaseCommand):
    help = "Validate unapproved posts using GPT and approve if clean."

    def handle(self, *args, **kwargs):
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

        posts = Post.objects.filter(is_approved=0)
        for post in posts:
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  # or gpt-4o if you have quota
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a content moderator. Label as Positive, Neutral, or Abusive.",
                        },
                        {"role": "user", "content": f"Check this post: {post.content}"},
                    ],
                    temperature=0,
                )
                result = response.choices[0].message.content.strip().lower()  # type:ignore
                if result in ["positive", "neutral"]:
                    post.is_approved = 1
                    post.save()
                    self.stdout.write(
                        self.style.SUCCESS(f"✅ Approved post {post.title}")
                    )
                else:
                    post.is_approved = 2
                    post.save()
                    self.stdout.write(
                        self.style.WARNING(f"🚫 Rejected post {post.title}")
                    )
            except Exception as e:
                self.stderr.write(
                    self.style.ERROR(f"❌ Error for post {post.title}: {str(e)}")
                )
"""
