from woob.core.woob import Woob

from amazon import AmazonModule

woob = Woob()

amazonModule = AmazonModule(woob, 'amazon',
                            config={'website': 'www.amazon.fr', 'email': 'ayoubennaoui358@gmail.com', 'password': "Tabahmout55'"})

browser = amazonModule.create_default_browser()

browser.do_login()

