<template>
  <div id="home">
    <h2 style="color: grey; margin-bottom: 50px;">Task Register</h2>
    <form>
      <div style="margin-bottom: 10px; text-align: left">
        <b-button v-if="phase===1" variant="primary" @click="addTask">Add Task</b-button>
        <b-button v-if="phase===1 && numTasks > 1" variant="danger" @click="removeTask" style="margin-left: 10px">Remove Task</b-button>
        <b-button v-else-if="phase===1" disabled variant="danger" @click="removeTask" style="margin-left: 10px">Remove Task</b-button>
		<b-button v-if="phase===2" variant="outline-primary" @click="reload">Reload</b-button>
      </div>

      <div v-if="phase===1">
        <HourField v-for="n in numTasks" :key="n" :index="n-1" :list="list" class="margin-top"/>
      </div>
      <div v-if="phase===2">
        <TaskInfo v-for="n in numTasks" :key="n" :index="n-1" :list="list" :time="list[n-1]" class="margin-top"/>
      </div>

      <b-button block variant="success" class="margin-top" @click="onSubmit">Submit</b-button>
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
    removeTask: function() {
      this.numTasks--;
    },
    reload: function() {
      this.numTasks = 1;
      this.list = [{}];
      this.phase = 1;
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
#home {
  display: inline-block;
  background-color: aliceblue;
  padding: 5px 20px 5px 20px;
}

.margin-top {
  margin-top: 10px;
}
</style>