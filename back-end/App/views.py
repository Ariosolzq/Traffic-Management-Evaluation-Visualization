from django.views import View
from django.http import JsonResponse
from App.models import Schoolprocess, Userinfo
from App.return_response import return_response
from django.http import FileResponse

from .models import Image

# cbv 基于类的视图，就是在视图里使用类处理请求
# 通过父类 View 提供的一个静态方法 as_view()
# as_view 方法是基于类的外部接口， 他返回一个视图函数，调用后请求会传递给 dispatch 方法，dispatch 方法再根据不同请求来处理不同的方法

# 用户登陆验证接口
class Login(View):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not all([username, password]):
            response = return_response(succ=False, error='用户信息不完整！')
        elif Userinfo.objects.filter(username=username, password=password).exists():
            t = Userinfo.objects.get(username=username)
            response = return_response(info='用户登陆成功！')
        else:
            response = return_response(succ=False, error='用户名或密码错误！')
        return JsonResponse(response)

# 查询总评分
class Query(View):
    # 返回学校名称和总评分
    def get(self, request):
        t = Schoolprocess.objects.all()
        data = []
        for row in t:
            data.append({
                'location': row.location,
                'sum': row.sum,
            })
        response = return_response(data=data)
        return JsonResponse(response)
    # 根据学校名称获取学校详细得分
    def post(self, request):
        location = request.POST.get("location")
        t = Schoolprocess.objects.get(location=location)
        data = {
            'ti': t.ti,
            'im': t.im,
            'im1': t.im1,
            'im2': t.im2,
            'im3': t.im3,
            'im4': t.im4,
            'im5': t.im5,
            'to': t.to,
            'to1': t.to1,
            'to2': t.to2,
            'to3': t.to3,
            'to4': t.to4,
            'to5':t.to5,
            'rs':t.rs,
            'rs1':t.rs1,
            'rs2':t.rs2,
            'sr':t.sr
        }
        response = return_response(data=data)
        return JsonResponse(response)

# 根据行政区划获得评分
class QuerybyRegion(View):
    def post(self, request):
        region = request.POST.get("region")
        try:
            records = Schoolprocess.objects.filter(region=region)
            data = []
            for record in records:
                data.append({
                    'location': record.location,
                    'sum': record.sum
                })
            response = return_response(data=data)
            return JsonResponse(response)
        except Exception as e:
            response = return_response(succ=False, error='An error occurred.')
            return JsonResponse(response)

import os

# 上传图片接口
class CreateImageView(View):
    def post(self, request):
        name = request.POST.get('name')
        image_file = request.FILES.get('image_file')

        if name is None or image_file is None:
            response = return_response(succ=False, error='缺少必要的字段！')
            return JsonResponse(response)

        # 创建子文件夹
        subfolder_path = os.path.join('media/image', name)
        image_path = os.path.join(subfolder_path, image_file.name)

        # 查询数据库以检查是否存在相同名称和路径的图像记录
        if Image.objects.filter(name=name, image_file=image_path).exists():
            response = return_response(succ=False, error='该路径下已有相同名称的图片！')
        else:
            os.makedirs(subfolder_path, exist_ok=True)
            with open(image_path, 'wb') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)
            image = Image(name=name, image_file=image_path)
            image.save()
            image_id = image.id
            # 添加成功后的处理逻辑
            info = '图片上传成功！'
            data = []
            data.append({
                'image_id': image_id
            })
            response = return_response(info=info, data=data)
        return JsonResponse(response)

# 删除图片接口
class DeleteImageView(View):
    def post(self, request):
        id = request.POST.get('id')
        if Image.objects.filter(id=id).exists():
            image = Image.objects.get(id=id)
            image_path = image.image_file.name
            print(image)
            print(image_path)
            # 删除数据库记录
            image.delete()

            # 删除图像文件
            os.remove(image_path)

            # 返回成功的响应
            response = {
                'info': '图片删除成功！'
            }
        else:
            response = {
                'info': '此id图片不存在！'
            }
        return JsonResponse(response)

# 显示图片接口
class GetImageView(View):
    def post(self, request):
        id = request.POST.get('id')
        if Image.objects.filter(id=id).exists():
            image = Image.objects.get(id=id)
            image_path = image.image_file.name
            response = FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
            return response
        else:
            response = {
                'info': '此id图片不存在！'
            }
            return JsonResponse(response)


class GetIdsBynameView(View):
    def post(self, request):
        name = request.POST.get('name')

        # 查询数据库获取匹配的id记录
        ids = Image.objects.filter(name=name).values_list('id', flat=True)

        # 将查询结果转换为列表
        id_list = list(ids)

        # 构建JSON响应
        response_data = {
            'data': id_list
        }

        return JsonResponse(response_data)