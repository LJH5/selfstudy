<template>
  <div class="border">
    <h1>이것은 내가 만든 새로운 컴포넌트다!!!</h1>
    <!-- 3. 등록하기 -->
    <MyComponentItem 
      kabab-case="맛있다!!!"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',
  // 2. 등록하기
  components: {
    MyComponentItem,
  },
  data: function () {
    return {
      dynamicProps: '이건 동적인 데이터!!!',
    }
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log('용돈 없어!!')
      console.log(childData)
    },
    getDynamicData: function (childInputData) {
      console.log(`사용자가 입력한 깂은 ${childInputData}입니다`)
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>