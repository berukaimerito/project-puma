DATABASES = {
    'default': {
      'ENGINE': 'djongo',
      'NAME': 'puma',
      'CLIENT': {
          'host': 'mongodb://mongodb:27017',
          'username': 'root',
          'password': 'root',
          'authSource': 'admin',
          'authMechanism': 'SCRAM-SHA-1',
      }
  }
}