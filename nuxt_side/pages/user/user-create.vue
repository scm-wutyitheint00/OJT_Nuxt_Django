<template>
  <div class="container">

    <v-form>
      <v-row>
        <h1 class="title">
          Create User
        </h1>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subheader>Name</v-subheader>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-text-field outlined v-model="user.name" label="Name" :rules="[required('name')]" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subheader>Email Address</v-subheader>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-text-field outlined v-model="user.email" label="Email" :rules="[required('email'), emailFormat()]"
            type="text" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subheader>Password</v-subheader>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-text-field outlined v-model="user.password" label="Password" type="password"
            :rules="[required('password')]" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subheader>Confirm Password</v-subheader>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-text-field outlined v-model="user.confirmPassword" label="Confirm Password" type="password"
            :rules="[required('confirmPassword')]" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subheader>Type</v-subheader>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-select :items="items" outlined v-model="user.type" :rules="[required('type')]"></v-select>
        </v-col>
      </v-row>

      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subheader>Phone</v-subheader>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-text-field outlined v-model="user.phone" label="Phone" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subheader>Date of Birth</v-subheader>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-dialog ref="dialog" v-model="user.modal" :return-value.sync="date" persistent width="290px">
            <template v-slot:activator="{ on, attrs }">
              <v-text-field v-model="user.dob" label="Pick a date" prepend-icon="mdi-calendar" readonly v-bind="attrs"
                v-on="on"></v-text-field>
            </template>
            <v-date-picker v-model="user.dob" scrollable>
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="user.modal = false">
                Cancel
              </v-btn>
              <v-btn text color="primary" @click="$refs.dialog.save(user.dob)">
                OK
              </v-btn>
            </v-date-picker>
          </v-dialog>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subheader>Address</v-subheader>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-textarea outlined v-model="user.address" label="Address" type="text" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subheader>Profile</v-subheader>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-text-field outlined v-model="user.profile" label="Profile" />
        </v-col>
      </v-row>
      <v-btn name="submit-btn" @click="confirmPost">Confirm</v-btn>
      <v-btn name="submit-btn" @click="clearData">Clear</v-btn>
    </v-form>
  </div>
</template>

<script>
import validations from '@/utils/validations'
export default {
  head() {
    return {
      title: "View Post"
    };
  },
  // items: () => ({
  //   items: [
  //     { title: 'Click Me' },
  //     { title: 'Click Me' },
  //     { title: 'Click Me' },
  //     { title: 'Click Me 2' },
  //   ],
  // }),
  async asyncData({ $axios, params }) {
    // let user = {
    //     name: '',
    //     email: '',
    //     password: '',
    //     confirmPassword: '',
    //     type: 1,
    //     phone: '',
    //     dob: '',
    //     address: '',
    //     profile: ''
    // }
  },
  data() {
    return {
      user: {
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
        type: '',
        phone: '',
        dob: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
        address: '',
        profile: '',
        // type: [admin, user],
        menu: false,
        modal: false,
        menu2: false,
      },
      items: ['Admin', 'User'],
      ...validations
    };
  },
  methods: {
    confirmPost() {
      console.log('user', this.user)
      // this.$router.push('/user/post_confirm');
      this.$router.push({ path: '/user/user-confirm' });
      // if(this.user.title && this.user.description) {
      this.$store.commit('ADD_USER', this.user)
      // }

    },
    clearData() {
      this.user.name = '';
      this.user.email = '';
      this.user.password = '',
        this.user.confirmPassword = '',
        this.user.type = '',
        this.user.phone = '',
        this.user.dob = '',
        this.user.address = '',
        this.user.profile = ''
    }
  }
};
</script>

<style scoped>
.col .col-8 {
  padding: 0 !important;
}
</style>