import { createRouter,createWebHashHistory } from "vue-router";
import ClockPage from '@/pages/ClockPage.vue'
import CountDown from '@/pages/CountDown.vue'
import SecondClock from '@/pages/SecondClock.vue'
import WorldClock from "@/pages/WorldClock.vue";
const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {
            name:'clockpage',
            path:'/ClockPage',
            component:ClockPage
        },
        {
            path:'/',
            redirect:'/ClockPage'
        },
        {
            name:'countdown',
            path:'/CountDown',
            component:CountDown
        },
        {
            name:'secondclock',
            path:'/SecondClock',
            component:SecondClock
        },
        {
            name:'worldclock',
            path:'/WorldClock',
            component:WorldClock
        }
    ]
})

export default router