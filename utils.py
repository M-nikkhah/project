from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin
def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('385536686E5176322F573648624B575A4F5931704E6F7957523341694A503634627456444F4166345873733D')
        params = {
            'sender': '',  # optional
            'receptor': phone_number,
            'message': f'کد تایید شما برای کتاب فروشی بی مرز {code}'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin