<template>
    <navbar
        @about="switchAbout"
        @articles="switchPosts"
        @exit="resetUser"
        :activeUser="user"
    ></navbar>
    <div class="app">
        <about 
            v-if="mode === 2"
        ></about>
        <post-page 
            @logged="setUser"
            @openpost="openPost"
            v-else-if="mode === 1"
            :activeUser="user"
        ></post-page>
        <post-id-page 
            v-else-if="mode === 3"
            :post="openedpost"
            :activeUser="user"
        ></post-id-page>

    </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import About from "@/pages/About";
import PostIdPage from "@/pages/PostIdPage";
import PostPage from "@/pages/PostPage";
export default {
    components: {
        Navbar,
        About,
        PostIdPage,
        PostPage
    },
    data() {
        return {
            mode: 1,
            user: 'Anon',
            openedpost: {
                'title':'',
                'description':'',
                'body':'',
                'author':'',
            },
        }
    },
    methods: {
        switchAbout() {
            this.mode = 2;
        },
        switchPosts() {
            this.mode = 1;
        },
        setUser(user) {
            this.user = user;
        },
        openPost(post) {
            this.openedpost.id = post.id;
            this.openedpost.title = post.title;
            this.openedpost.description = post.description;
            this.openedpost.body = post.body;
            this.openedpost.author = post.author;
            this.mode = 3;
        },
        resetUser() {
            this.user = 'Anon';
        }

    }
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.app {
    padding: 20px;
}
</style>