from distutils.core import setup
setup(
  name = 'instagram-follow',
  packages = ['instagram_follow', 'instagram_follow.bot', 'instagram_follow.api'],
  version = '0.1',
  description = 'Instagram scripts and API python wrapper.',
  author = 'Igor Khripchenko',
  author_email = 'ikhripchenko@gmail.com',
  url = 'https://github.com/khrigo/instagram-follow',
  download_url = 'https://github.com/khrigo/instragram-follow/releases',
  keywords = ['instagram', 'bot', 'api', 'wrapper'],
  classifiers = [],
  install_requires=['tqdm', 'requests-toolbelt', 'requests'],
)
