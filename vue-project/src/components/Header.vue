<template>
  <nav>
    <ul class="nav justify-content-center">
      <li class="nav-item">
        <a class="nav-link" href="#">
          <router-link to="/kakaomap">
            카카오맵
          </router-link>
        </a>
      </li>
      <li class="nav-item">
          <router-link to="/">BS
        <span>bakery Studio</span>
      </router-link>
      </li>
      <li class="nav-item">
        <router-link to="/board/postlist">
          <a class="nav-link" href="#">
            게시판
          </a>
        </router-link>
      </li>
    </ul>
  </nav>
</template>
<script>
export default{
    name: "Header"
}
</script>
<style scoped>
li{list-style:none;
  font-size:20px;;}
nav{width:100%;
  background-color: black;
  position:fixed;
  z-index:999;
    margin:0 auto;}
a{text-decoration:none;
 color:white;
 }
 a:hover{font-weight:700;
         color:rgb(182, 139, 73);}

          .nav-item{text-align: center;}

span{display:block;
           font-size:28px;}

.disabled{text-align: center;
          font-size:24px;}

ul li:nth-child(1){margin-top:10px;}
ul li:nth-child(3){margin-top:10px;}
ul li:nth-child(2) a:hover{color:white;}

li{float:left;
  padding:10px;}

@media screen and (max-width:1000px){
li{font-size:16px;;}
.disabled{font-size:16px;}
span{font-size:20px;;}
}

</style>
