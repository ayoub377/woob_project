from woob.core.woob import Woob

woob = Woob()

backend = woob.build_backend('amazon', {
    'website': 'www.amazon.fr',
    'email': 'email',
    'password': 'password',
})

