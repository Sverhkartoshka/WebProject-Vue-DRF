<template>
    <div>
        <h1>{{ post.title }}</h1>
        <div>Автор: {{ post.author }}</div>
        <h3>{{ post.description }}</h3>
        <div>{{ post.body }}</div>
    </div>
    <my-button 
        v-if="activeUser != 'Anon'"
        @click="showForm"
    >
        Создать комментарий
    </my-button>
    <my-dialog v-model:show="dialogVisible">
        <comments-form
            @create="createComment"
            :curuser="activeUser"
        />
    </my-dialog>
    <comment-list 
        :comments="comments"
        :curuser="activeUser"
        @remove="removeComment"
    />
</template>

<script>
import CommentsForm from "@/components/CommentsForm";
import CommentList from "@/components/CommentList";
import axios from 'axios';
import MyInput from "@/components/UI/MyInput";
import MyButton from "@/components/UI/MyButton";

export default {
    components: {
        CommentList, 
        CommentsForm,
        MyInput,
        MyButton
    },
    props: {
        post: Object,
        activeUser: String,
    },
    data() {
        return {
            comments: [],
            dialogVisible: false,
        }
    },
    methods: {
        async fetchComments() {
            const response = await axios.get(`http://127.0.0.1:8000/api/comments/${encodeURIComponent(this.post.id)}`)
            this.comments = response.data.comments;
        },
        async createComment(comment) {
            const res = await axios.post('http://127.0.0.1:8000/api/comments/', { comment_add: comment });
            this.dialogVisible = false;
            this.fetchComments();
        },
        async removeComment(comment) {
            const res = await axios.delete(`http://127.0.0.1:8000/api/comments/${encodeURIComponent(comment.id)}`);
            this.fetchComments();
        },
        showForm() {
            this.dialogVisible = true;
        },
    },
    mounted() {
        this.fetchComments();
    },
}
</script>

<style scoped>

</style>