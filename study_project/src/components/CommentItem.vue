<template>
    <div class="comment">
        <div>
            <div><strong>Автор: </strong>{{ comment.author }}</div>
            <div> {{ comment.body }}</div>
        </div>
        <div class="com__btns">
            <my-button 
                @click="$emit('remove', comment)"
                v-if="comment.author === curuser"
            >
                Удалить
            </my-button>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        comment: {
            type: Object,
            required: true,
        },
        curuser: String,
    },
}
</script>

<style scoped>
    .comment {
        padding: 15px;
        margin-top: 15px;
        border: 2px solid teal;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .com__btns {
        display: flex;
    }
</style>