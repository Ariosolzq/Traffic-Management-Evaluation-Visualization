import axios from 'axios';

// axios.headers["Content-Type"] = "mutipart/form-data";
//import { Message } from 'element-plus'
// const headers = { 'content-type': 'application/x-www-form-urlencoded' };

axios.defaults.headers["Content-Type"] = "application/x-www-form-urlencoded";
export default function request(config) {
    const instance = axios.create({
        baseURL: '/api',
        timeout: 7000,
        // header: headers,
    });

    instance.interceptors.request.use(config => {
        //axios.defaults.headers["Content-Type"] = "mutipart/form-data";
        //config.contenType='form/data';
        return config;
    }, err => {
        console.log(err);
    });

    instance.interceptors.response.use(res => {
        return res.data;
    }, err => {
        console.log(err);
        return Promise.reject(err);
    })
    return instance(config)
}
