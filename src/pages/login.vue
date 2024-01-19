<template>
    <div>
        <el-row class="login-container">
            <!-- flex容器可以对各大浏览器进行兼容 -->
            <el-col :lg="16" :md="12" class="left">
                <div>
                    <div>Welcome</div>
                    <div class="showabout">此站点是“学医景商”平台的展示</div>
                    <div>请在右边完成登录后查看吧！</div>
                </div>
            </el-col>
            <el-col :lg="8" :md="12" class="right ">
                <h2 class="title">欢迎回来</h2>
                <div>
                    <span class="line"></span>
                    <span>账号密码登录</span>
                    <span class="line"></span>
                </div>
                <el-form ref="formRef" :rules="rules" :model="form" class="w-[250px]">
                    <el-form-item prop="username">
                        <el-input v-model="form.username" placeholder="请输入用户名">
                            <template #prefix>
                                <el-icon><User /></el-icon>
                        </template>
                        </el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input type="password" v-model="form.password" 
                        placeholder="请输入密码" show-password>
                        <template #prefix>
                            <el-icon><Lock /></el-icon>
                        </template>
                        </el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button round color="#475569" class="w-[250px]" type="primary" @click="onSubmit">登 录</el-button>
                    </el-form-item>
                </el-form>
            </el-col>
        </el-row>
    </div>
</template>

<!-- 单文件组件中使用组合式API的编译时语法糖 -->
<script setup>
import { ref,reactive } from 'vue'
// import { login } from '~/api/manager' 
import { ElNotification } from 'element-plus'
import { useRouter } from 'vue-router'
import { Login_t } from '~/network/home'

const router=useRouter()

const form = reactive({
    username:"",
    password:""
})

const rules={
    username:[
    { 
        required: true, 
        message: '用户名不能为空', 
        trigger: 'blur' 
    },
    ],
    password:[
    { 
        required: true, 
        message: '密码不能为空', 
        trigger: 'blur' 
    },
    ]
}

// 使用ref让表单验证变成响应式的
const formRef=ref(null)

const onSubmit = () => {
    formRef.value.validate((valid) => {
        if (!valid) {
            return false
        }
        Login_t(form)
        .then(res => {
            // 检查返回的数据中的成功标志
            if (res.succ) {
                // 提示成功
                ElNotification({
                    message: res.info || "登录成功！",
                    type: 'success',
                    duration: 3000
                })

                // 跳转到后台首页
                router.push("/index")
            } else {
                ElNotification({
                    message: res.errs || "登录失败！",
                    type: 'error',
                    duration: 3000
                })
            }
        })
        .catch(err => {
            ElNotification({
                message: err.message || "请求失败！",
                type: 'error',
                duration: 3000
            })
        })
    })
}
</script>


<style scoped>
.login-container{
    @apply min-h-screen bg-slate-600;
}
.login-container .left,.login-container .right{
    @apply flex items-center justify-center;
}
.login-container .right{
    @apply  bg-light-50 flex-col;
}
.left>div>div:first-child{
    @apply font-bold text-6xl text-light-50 mb-4;
}

.left>div>div:last-child{
    @apply text-gray-200 font-bold text-sn mb-2;
}

.left .showabout{
    @apply text-gray-200 text-sn mb-2;
}

.right .title{
    @apply font-bold text-4xl text-gray-800;
}

.right>div{
    @apply flex items-center justify-center my-5 text-gray-300 space-x-2;
}

.right .line{
    @apply h-[1px] w-16 bg-gray-200;
}

</style>