<template>
  <div id="task-info">
    <input type="time" v-model="time" disabled="true" class="margin-right">
    <input type="date" v-model="date" @change="change" class="margin-right">
    <input v-model="task" @change="change" placeholder="Task Num" required class="margin-right">
    <input v-model="comment" @change="change" placeholder="Comment" required >
  </div>
</template>

<script>
export default {
  name: 'TaskInfo',
  props: ['index', 'list', 'time'],
  components: {},
	data () {
    return {
      task: null,
      comment: null,
      date: new Date().toISOString().substr(0, 10)
    }
  },
  methods: {
    change: function() {
      this.list[this.index] = {
        task: this.task,
        comment: this.comment,
        time: this.time,
        date: this.date
      }
      console.log(this.list)
    }
  }
}
</script>

<style scoped>
.margin-right {
  margin-right: 5px;
}
</style>