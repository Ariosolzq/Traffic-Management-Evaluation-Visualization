import {
    createRouter,
    createWebHashHistory
} from 'vue-router'

import Index from '~/pages/index.vue'
import Login from '~/pages/login.vue'
import NotFound from '~/pages/404.vue'
// import Indextst from '~/pages/indextst.vue'

//实现路由切换的配置
const routes = [{
    path:"/",
    component:Login
},
{
    path:"/index",
    component:Index
},
{
    path:"/:pathMatch(.*)*",
    name:'NotFound',
    component:NotFound
}]
const router = createRouter({
    history:createWebHashHistory(),
    routes
})

export default router

