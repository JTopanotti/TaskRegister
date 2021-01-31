<template>
  <div id="home">
    <h2>Task Register</h2>
    <form>
      <div v-if="phase===1">
        <HourField v-for="n in numTasks" :key="n" :index="n-1" :list="list" class="margin-top"/>
      </div>
      <div v-if="phase===2">
        <TaskInfo v-for="n in numTasks" :key="n" :index="n-1" :list="list" :time="list[n-1]" class="margin-top"/>
      </div>

      <div class="margin-top">
        <b-button variant="primary" @click="onSubmit">Submit</b-button>
        <b-button v-if="phase===1" variant="primary" @click="addTask" style="margin-left: 10px">Add Task</b-button>
      </div>
    </form>
  </div>
</template>

<script>
import HourField from './HourField.vue'
import TaskInfo from './TaskInfo.vue'
import axios from 'axios'

export default {
  name: 'Home',
  components: { HourField, TaskInfo},
  data() {
    return {
      date: Date.now(),
      numTasks: 1,
      list: [{}],
      phase: 1
    }
  },
  methods: {
    addTask: function() {
      this.numTasks++
    },
    onSubmit: function() {
      if (this.phase === 2) {
        axios.post('/register', this.list, { headers: { 'Content-Type':'application/json' } }).then(resp => {
          console.log(resp)
        })
      } else 
        this.phase++
    }
  }
}
</script>

<style scoped>
.margin-top {
  margin-top: 10px;
}
</style>