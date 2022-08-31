<template>
    <div class="container">
        <v-form>
            <v-row>
                <h1 class="title">
                    Edit User
                </h1>
            </v-row>
            <v-row>
                <v-col class="ma-0 pa-3" cols="2">
                    <v-subtitle>Name</v-subtitle>
                </v-col>
                <v-col class="ma-0 pa-3" cols="8">
                    <v-text-field outlined v-model="user.name" label="Name" :rules="[required('name')]" />
                </v-col>
            </v-row>
            <v-row>
                <v-col class="ma-0 pa-3" cols="2">
                    <v-subtitle>Email Address</v-subtitle>
                </v-col>
                <v-col class="ma-0 pa-3" cols="8">
                    <v-text-field outlined v-model="user.email" label="Email"
                        :rules="[required('email'), emailFormat()]" type="text" />
                </v-col>
            </v-row>
            <v-row>
                <v-col class="ma-0 pa-3" cols="2">
                    <v-subtitle>Password</v-subtitle>
                </v-col>
                <v-col class="ma-0 pa-3" cols="8">
                    <v-text-field outlined v-model="user.password" label="Password" type="password"
                        :rules="[required('password')]" />
                </v-col>
            </v-row>
            <v-row>
                <v-col class="ma-0 pa-3" cols="2">
                    <v-subtitle>Type</v-subtitle>
                </v-col>
                <v-col class="ma-0 pa-3" cols="8">
                    <v-select :items="items" outlined v-model="user.type" ></v-select>
                </v-col>
            </v-row>

            <v-row>
                <v-col class="ma-0 pa-3" cols="2">
                    <v-subtitle>Phone</v-subtitle>
                </v-col>
                <v-col class="ma-0 pa-3" cols="8">
                    <v-text-field outlined v-model="user.phone" label="Phone" />
                </v-col>
            </v-row>
            <v-row>
                <v-col class="ma-0 pa-3" cols="2">
                    <v-subtitle>Date of Birth</v-subtitle>
                </v-col>
                <v-col class="ma-0 pa-3" cols="8">
                    <v-dialog ref="dialog" v-model="user.modal" :return-value.sync="user.dob" persistent width="290px">
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field clearable @click:clear="user.dob = null" v-model="user.dob"
                                label="Pick a date" prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on">
                            </v-text-field>
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
                    <v-subtitle>Address</v-subtitle>
                </v-col>
                <v-col class="ma-0 pa-3" cols="8">
                    <v-textarea outlined v-model="user.address" label="Address" type="text" />
                </v-col>
            </v-row>
            <v-row>
                <v-col class="ma-0 pa-3" cols="2">
                    <v-subtitle>Profile</v-subtitle>
                </v-col>
                <v-col class="ma-0 pa-3 text-left" cols="8">
                    <input type="file" accept=".jpeg,.jpg,.png,image/jpeg,image/png" aria-label="upload image button"
                        @change="selectFile" />
                </v-col>
            </v-row>
            <v-btn name="submit-btn" @click="updatePost">Update</v-btn>
        </v-form>
    </div>
</template>
  
  <script>
import validations from '@/utils/validations'
export default {
    head() {
        return {
            title: "View Post",
        };
    },

    async asyncData({ $axios, params }) {
        try {

            let user = await $axios.$get(`/users/${params.id}`);
            user.type = user.type === 1 ? 'Admin' : 'User';
            return { user };
        } catch (e) {
            return { user: [] };
        }

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
                dob: '',
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
        async updatePost() {
            let userData = this.user;
            userData.updated_user_id = 1;
            userData.created_at = new Date().toISOString();
            userData.updated_at = new Date().toISOString();
            userData.type = userData === 'Admin' ? 1 : 2;
            Object.keys(userData).forEach(key => {
                if (userData[key] === null) {
                    delete userData[key];
                }
            });
            const config = {
                headers: { "content-type": "multipart/form-data" }
            };
            let formData = new FormData();
            console.log(this.user.profile)
            for (let data in userData) {
                formData.append(data, userData[data]);
                if (typeof this.user.profile === 'string') {
                    this.$delete(userData, 'profile');
                } else {
                    formData.append("file", this.user.profile);
                }
            }
            try {
                let response = await this.$axios.$patch(`/users/${userData.id}/`, formData, config);
                this.$router.push("/post/");
            } catch (e) {
                console.log(e);
            }
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
        },
        async selectFile(e) {
            const file = e.target.files[0];
            if (!file) return;
            this.user.profile = file;
        }
    }
};
</script>
  
  <style scoped>
  .col .col-8 {
      padding: 0 !important;
  }
  </style>