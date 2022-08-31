<template>
    <v-app>
        <v-app-bar app color="green">
            <v-toolbar-title>Bulletin Board</v-toolbar-title>
            <v-btn v-if="$auth.loggedIn" text to="/post">Posts</v-btn>
            <v-btn v-if="($store.state.isMember === true || isMember === 'true') && $auth.loggedIn" text
                to="/user/profile">User</v-btn>
            <v-btn v-if="$auth.loggedIn" text to="/user">Users</v-btn>
            <v-spacer />
            <div v-if="$auth.loggedIn">
                {{  $auth.user.email  }}
                <v-btn text to="/" @click="logout()">Logout</v-btn>
            </div>
            <div v-else>
                <v-btn text to="/login">Login</v-btn>
                <v-btn text to="/register">Register</v-btn>
            </div>
        </v-app-bar>
        <main>
            <Nuxt />
        </main>
        <v-dialog v-model="showDialog" persistent max-width="400">
            <v-card>
                <v-card-title><span class="text-subtitle-1 text--primary">As login time is passed 1 hour, please login
                        again..</span></v-card-title>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="green darken-1" text @click="showDialog = false">
                        OK
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-app>
</template>
<script>
export default {
    created() {
        const lastOperationDate = localStorage.getItem('lastOperationDate');
        this.sectionTime = lastOperationDate;
        this.isMember = localStorage.getItem("isMember");
        if (!lastOperationDate) {
            return
        }
        const operationtime = Date.now() - new Date(lastOperationDate).getTime();
        const inHour = Math.floor(operationtime / (1000 * 60 * 60));
        if (inHour > 1) {
            this.$auth.logout();
            localStorage.clear();
            this.showDialog = true
        }
    },
    data() {
        return {
            showDialog: false,
            sectionTime: null,
            isMember: null
        }
    },
    async asyncData({ $axios, params }) {
        // try {
        let isMember = localStorage.getItem("isMember");
        return { isMember };
    },
    methods: {
        logout() {
            this.$auth.logout();
            localStorage.clear();
            localStorage.removeItem('isMember');
            localStorage.removeItem('loginEmail');
            this.$store.commit('SET_MEMBER', '');
        }
    }
}
</script>
<style>
:root {
    --primary-color: #00c58e;
    font-size: 0.9em;
}

body {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto,
        Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji,
        Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
    margin: 0;

}

a {
    color: inherit;
    text-decoration: none;
}

nav a:hover {
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

v-app {
    margin: 0 auto;

    padding: 0 1rem;
    max-width: 1280px;
}

main {
    padding-top: 100px;
    background-color: rgb(186, 248, 218);
    text-align: center;
    height: 100%;
}

a.v-btn,
.v-toolbar__title {
    margin-left: 25px;
}

a.nuxt-link-exact-active {
    color: #00c58e;
}
</style>
