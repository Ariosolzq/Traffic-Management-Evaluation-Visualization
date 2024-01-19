import request from './requests';

//登录
export  function Login_t(params) {
    return request({
        url: 'Login/',
        method:'post',
        data:params
    })
}

export  function Initial(params) {
    return request({
        url: 'Query/',
        method:'get',
        data:params
    })
}

export  function Region(params) {
    return request({
        url: 'QuerybyRegion/',
        method:'post',
        data:params
    })
}

export  function Detail(params) {
    return request({
        url: 'Query/',
        method:'post',
        data:params
    })
}

// 图片上传
export function ImageCreate(params) {
    let formData = new FormData(); // 创建一个新的 FormData 对象，用于封装表单数据。
    formData.append('name', params.name); // 将参数中的学校名称添加到表单数据中。
    formData.append('image_file', params.image_file); // 将参数中的图片文件添加到表单数据中。

    return request({
      url: 'image/create/', // 指定请求的 URL。
      method: 'post', // 指定请求方法为 POST。
      data: formData, // 将表单数据作为请求体发送。
      headers: {
        'Content-Type': 'multipart/form-data' // 设置请求头的内容类型为 multipart/form-data，表示发送的数据是表单数据。
      }
    });
}

export function getIdList(params) {
    return request({
        url: 'idlist/',
        method: 'post',
        data: params
    });
}


export function searchImage(params) {
    return request({
        url: 'image/search/',
        method: 'post',
        data: params,
        responseType: 'blob' // 表示返回的数据是一个 Blob 对象，适用于文件内容
    });
}

export function deleteImage(params) {
    return request({
      url: 'image/delete/',
      method: 'post',
      data: params
    });
  }



// vue组件中使用：
/*
1.先引入getHomeData
2.然后在要使用的地方：
getHomeData().then(res => {
    if (res.succ) {
        this.homeData = res.data
        this.$message.success(res.info)
    } else {
        this.$message.error(res.errs)
    }



    {
        succ: true,
        info: "",
        errs: "",
        data: []
    }
}).catch(err => {
    err == 请求失败之后在这里处理
})
*/