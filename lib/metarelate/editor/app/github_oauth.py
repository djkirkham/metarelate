from social.backends.github import GithubOAuth2

class MrGithubOAuth2(GithubOAuth2):
     def get_user_details(self, response):
        """Return user details from Github account"""
        return {'username': response.get('html_url'),
                'email': response.get('email') or '',
                'fullname': response.get('login'),
                'token': response.get('access_token')}
