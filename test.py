from popcornnotify import notify

notify('5555555555', 'New user sign up', api_key='*******')
notify('team@popcornnotify.com', 'Memory exceeded...', subject='Staging Error', api_key='*******')
notify(['555...', 'team@...', 'dave@...'], "I'm sorry, Dave. I'm afraid I can't do that.", api_key='*******')
