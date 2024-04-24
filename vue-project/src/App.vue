<template>
  <div id="app">
    <Header />
    <div id="content" class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import { RouterView } from 'vue-router';
import Header from '@/components/Header.vue'

export default{
    components:{
      Header
    },
  
}
</script>
<style scoped>

</style>

