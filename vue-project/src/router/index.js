import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import PostList from '@/components/board/PostList.vue'
import KakaoMap from '@/components/KakaoMap.vue'
import PostDetail from '@/components/board/PostDetail.vue'
import PostWrite from '@/components/board/PostWrite.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
     {
       path:'/KakaoMap',
       name:'KakaoMap',
       component: KakaoMap
     },
    {
    path:'/board/postlist',
    name:'PostList',
    component: PostList
    },
    {
      path: '/board/postdetail',
    name: 'PostDetail',
      component: PostDetail
    },
    {
      path: '/board/PostWrite',
    name: 'PostWrite',
      component: PostWrite
    }
  ]
  
})

export default router
