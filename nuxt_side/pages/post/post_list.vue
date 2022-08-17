
<template>
    <v-data-table 
    :headers="headers" 
    :items="desserts" 
    :items-per-page="10" 
    hide-default-footer
    class="elevation-1"></v-data-table>
</template>

<script>
window.axios=require('axios');

export default {
    
    data() {
        return {
            headers: [
                {
                    text: 'Post Title',
                    align: 'start',
                    sortable: false,
                    value: 'title'
                },
                { text: 'Post Description', value: 'description' },
                { text: 'Posted User', value: 'create_user_id' },
                { text: 'Posted Date', value: 'created_at' },
                { text: '', value: 'edit' },
                { text: '', value: 'delete' },
            ],
            desserts: []
        }
    },
    async asyncData({ $axios, params }) {
        // try {
            let posts = await $axios.$get(`/posts/`);
            const desserts = posts.map(p => p.fields)
            return { desserts };
        // } catch (e) {
        //     return { desserts: [] };
        // }
    },
    //   data() {
    //     return {
    //       recipes: []
    //     };
    //   },
}
</script>

<style scoped>
  .v-data-table {
    font-size: 6em;
  }
</style>