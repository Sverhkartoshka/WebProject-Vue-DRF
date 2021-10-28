<template>
    <div class="post">
        <div @click="openPost">
            <div><strong>Название: </strong>{{ post.title }}</div>
            <div><strong>Описание: </strong> {{ post.description }}</div>
        </div>
        <div class="post__btns">
            <my-button 
                @click="$emit('remove', post)"
                v-if="post.author === curuser"
            >
                Удалить
            </my-button>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        post: {
            type: Object,
            required: true,
        },
        curuser: String,
    },
    methods: {
        openPost() {
            this.$emit('openpost', this.post);
        }
    }
}
</script>

<style scoped>
    .post {
        padding: 15px;
        margin-top: 15px;
        border: 2px solid teal;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .post__btns {
        display: flex;
    }
</style>