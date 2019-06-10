# coding=utf-8
# 李路
from cryptography.fernet import Fernet
#加密
def jiami():
    c = Fernet.generate_key()
    message1 = b'Lilu329297!@#'
    message2 = b'ali-rds-01-o.sqlserver.rds.aliyuncs.com,3433'
    message3 = b'192.168.1.40,1433'
    message4 = b'Qq123456!@#'
    message5 = b'ali-rds-02-o.sqlserver.rds.aliyuncs.com,3433'
    cc=Fernet(c)
    print(c)
    print(cc.encrypt(message1))
    print(cc.encrypt(message2))
    print(cc.encrypt(message3))
    print(cc.encrypt(message4))
    print(cc.encrypt(message5))
#解密
def jiemi():
    c=b'6YFaqNPkwWDusgPJM3v5cRDbKqUg-Nw8u7B8Qh6mh3Y='
    c1=b'gAAAAABc5nXiWzSBKu1rEF0Fqoekiq9yz0y3lLD3VhBEKR7yutdEZABhzZjEyF4J_eLROGkJ9RSwtKJfOsfv0hbrYE7083HChg=='
    c2=b'gAAAAABc5nXiFtqNx5uaug3IyPJrhU8I9qx8PXB-UHOB6VgkZdUMdT6jDJXA2P5PaVeNSciSd8OKSD4WbdaYg0Da154ShrowTIT6e_l7-zBabMxXm2lXBHlv7JwtMzZA4YF5LKCw1JGD'
    c3=b'gAAAAABc5nXisPyo3u9Ya2X2lZoAiYCxtQ_RhMQWLQX2ldUwb55qvDoj_y9X0W2PH4AEbZzEEMlQnucGYdB6EukKMdk7NJgqgKyQ0_AJ-bkTblX3VDnIVqk='
    c4=b'gAAAAABc5nXiYG5R-Rc7gxzvdq0nC4wXnpN-T6F4wG2FzQeIM6clfTAvJ5DtgLzy2qx_wPveQyoeIXsfXSM8inU6OxN1t6kuuA=='
    c5=b'gAAAAABc5nXiomDh-oOluAiWavETSudjw15PlkQ34NvsMLvwCsF1ZS_JNowlAFAHuIrtDEQUBQXF6N_mqgrKjiVmlw4WyFlHBl9TysyC-yGfJwOTPfIHd7530FdupTYRf2L1zTtr0hnX'
    cc=Fernet(c)
    print(cc.decrypt(c1))
    print(cc.decrypt(c2))
    print(cc.decrypt(c3))
    print(cc.decrypt(c4))
    print(cc.decrypt(c5))
jiemi()