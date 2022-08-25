<template>
  <div class="container">
    <h1>
      User List
    </h1>
    <v-row>
      <v-col cols="2.5">
        <v-text-field v-model="searchData.name" label="Name" />
      </v-col>
      <v-col cols="2.5">
        <v-text-field v-model="searchData.email" label="Email" />
      </v-col>
      <v-col cols="2.5">
        <v-dialog ref="dialog" v-model="searchData.modal" :return-value.sync="searchData.created_from" persistent
          width="290px">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field clearable @click:clear="searchData.created_from = null" v-model="searchData.created_from"
              label="Created From" prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on"></v-text-field>
          </template>
          <v-date-picker v-model="searchData.created_from" scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="searchData.modal = false">
              Cancel
            </v-btn>
            <v-btn text color="primary" @click="$refs.dialog.save(searchData.created_from)">
              OK
            </v-btn>
          </v-date-picker>
        </v-dialog>
      </v-col>
      <v-col cols="2.5">
        <v-dialog ref="dialog2" v-model="searchData.modal2" :return-value.sync="searchData.created_to" persistent
          width="290px">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field clearable @click:clear="searchData.created_to = null" v-model="searchData.created_to"
              label="Created To" prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on"></v-text-field>
          </template>
          <v-date-picker v-model="searchData.created_to" scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="searchData.modal2 = false">
              Cancel
            </v-btn>
            <v-btn text color="primary" @click="$refs.dialog2.save(searchData.created_to)">
              OK
            </v-btn>
          </v-date-picker>
        </v-dialog>
      </v-col>
      <v-col cols="1">
        <v-btn @click="searchUser()" name="submit-btn">Search</v-btn>
      </v-col>
      <v-col cols="1">
        <v-btn name="submit-btn" @click="addUser">Add</v-btn>
      </v-col>
    </v-row>
    <v-data-table :headers="headers" :items="users" :page.sync="page" :items-per-page="itemsPerPage" hide-default-footer
      @page-count="pageCount = $event" class="elevation-1">\
      <template v-slot:[`item.name`]="{ item }">
        <a href="#" @click="showUserDetail(item.id)">{{ item.name }}</a>
      </template>
      <template v-slot:[`item.email`]="{ item }">
        {{ item.email }}
      </template>
      <template v-slot:[`item.updated_user_id`]="{ item }">
        {{ item.updated_user_id }}
      </template>
      <template v-slot:[`item.phone`]="{ item }">
        {{ item.phone }}
      </template>
      <template v-slot:[`item.dob`]="{ item }">
        {{ item.dob }}
      </template>
      <template v-slot:[`item.address`]="{ item }">
        {{ item.address }}
      </template>
      <template v-slot:[`item.created_at`]="{ item }">
        {{ item.created_at }}
      </template>
      <template v-slot:[`item.updated_at`]="{ item }">
        {{ item.updated_at }}
      </template>
      <template v-slot:[`item.delete`]="{ item }">
        <a @click="deleteUser(item.id)">Delete</a>
      </template>
    </v-data-table>
    <div class="text-center pt-2">
      <v-pagination v-model="page" :length="pageCount"></v-pagination>
    </div>

    <v-dialog v-model="detailDialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="text-h5">User Detail</span>
        </v-card-title>
        <v-card-text>
          <v-container fill-height fluid>
            <v-row justify="center">
              <v-col cols="3">
                <span class="text-subtitle-1 text--primary">Name</span>
              </v-col>
              <v-col cols="7">
                <span class="text-subtitle-1 text--primary">{{this.userDetail.name}}</span>
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-col cols="3">
                <span class="text-subtitle-1 text--primary">Email</span>
              </v-col>
              <v-col cols="7">
                <span class="text-subtitle-1 text--primary">{{this.userDetail.email}}</span>
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-col cols="3">
                <span class="text-subtitle-1 text--primary">Birth Date</span>
              </v-col>
              <v-col cols="7">
                <span class="text-subtitle-1 text--primary">{{this.userDetail.dob}}</span>
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-col cols="3">
                <span class="text-subtitle-1 text--primary">Phone</span>
              </v-col>
              <v-col cols="7">
                <span class="text-subtitle-1 text--primary">{{this.userDetail.phone}}</span>
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-col cols="3">
                <span class="text-subtitle-1 text--primary">Address</span>
              </v-col>
              <v-col cols="7">
                <span class="text-subtitle-1 text--primary">{{this.userDetail.address}}</span>
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-col cols="3">
                <span class="text-subtitle-1 text--primary">Profile</span>
              </v-col>
              <v-col cols="7">
                <span class="text-subtitle-1 text--primary">{{this.userDetail.profile}}</span>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="detailDialog = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
window.axios = require('axios');

export default {

  data() {
    return {
      page: 1,
      pageCount: 0,
      itemsPerPage: 7,
      detailDialog: false,
      userDetail: {},
      headers: [
        {
          text: 'Name',
          align: 'start',
          sortable: false,
          value: 'name'
        },
        { text: 'Email', value: 'email' },
        { text: 'Created User', value: 'updated_user_id' },
        { text: 'Phone', value: 'phone' },
        { text: 'Birth Date', value: 'dob' },
        { text: 'Address', value: 'address' },
        { text: 'Created Date', value: 'created_at' },
        { text: 'Updated Date', value: 'updated_at' },
        { text: '', value: 'edit' },
        { text: '', value: 'delete' },
      ],
      users: [],
      searchData: {
        name: '', email: '', created_from: '', created_to: '', menu: false,
        modal: false,
        modal2: false,
        menu2: false,
      },
    }
  },

  async asyncData({ $axios, params }) {
    // try {
    let users = await $axios.$get(`/users/`);
    users.edit = true;
    users.delete = true;
    return { users };
  },
  methods: {
    addUser() {
      this.$router.push('/user/user-create');
    },
    async deleteUser(user_id) {
      try {
        await this.$axios.$delete(`/users/${user_id}/`); // delete recipe
        let remainUser = await this.$axios.$get("/users/"); // get new list of recipes
        this.users = remainUser; // update list of recipes
      } catch (e) {
        console.log(e);
      }
    },
    async searchUser() {
      let searchUser = await this.$axios.
        $get(`/users?name=${this.searchData.name}&email=${this.searchData.email}`);
      console.log('search user', searchUser)
      this.users = searchUser.filter(user => {
        if (this.searchData.created_from && !this.searchData.created_to) {
          if (user.created_at > this.searchData.created_from) {
            return user
          }
        } else if (!this.searchData.created_from && this.searchData.created_to) {
          if (user.created_at < this.searchData.created_to) {
            return user
          }
        } else if (this.searchData.created_from && this.searchData.created_to) {
          console.log('both')
          if (this.searchData.created_from < user.created_at && user.created_at < this.searchData.created_to) {
            return user
          }
        } else {
          return user
        }

      })
    },
    async showUserDetail(userId) {
      this.userDetail = await this.$axios.$get(`/users/${userId}`);
      this.detailDialog = true;
    }
  }
}
</script>

<style scoped>
h1 {
  margin-bottom: 50px;
}

a {
  color: blue;
  text-decoration: underline;
}
</style>