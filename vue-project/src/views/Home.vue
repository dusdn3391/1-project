<template>
  <div id="wrap">
    <div class="bg"></div>
    <div class="baker">
      <img src="../static/제빵사.png" alt="제빵사">
      <div class="text">
        <p>맛있는 빵이 
          <br/>기다리고 있어요~</p>
      </div>
    </div>
    <div class="kakaomap_ad"></div>
    <div class="post_ad"></div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
#wrap {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 56.25%; /* 원하는 비율로 수정하세요 */
  overflow: hidden;
}

.bg {
  width: 100%;
  background-image: url("../static/bakery.jpg");
  background-repeat: no-repeat;
  background-size: cover; /* 이미지를 화면에 꽉 채우도록 설정 */
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.baker img {
  width: 10%;
  position: absolute;
  top: 60%;
  left: 0;
}

.text {
  width: 100px;
  height: 50px;
  background-color: white;
  position: absolute;
  border-radius: 50%;
  top: 55%;
  left: 8%;
}

p {
  font-size: 0.7rem;
  margin-top: 8px;
  text-align: center;
}

.baker img {
  animation: motion 0.3s linear 0s infinite alternate;
  margin-top: 0;
}

@keyframes motion {
  0% {
    margin-top: 0px;
  }
  100% {
    margin-top: -50px;
  }
}

.text {
  animation: motion 0.3s linear 0s;
  margin-top: 0;
}

@keyframes motion {
  0% {
    margin-top: 0px;
  }
  100% {
    margin-top: -50px;
  }
}
</style>
