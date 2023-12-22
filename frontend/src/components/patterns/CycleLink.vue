<template>
    <div class="task-cycle-link">
        <div class="title"> {{ cycle.title }}</div>
        <div class="class-number">Класс: 9</div>
        <div class="deadline">Дедлайн: 10.01.2023</div>
        <div class="submit" @click.prevent="changePage('SubmitPage', {submitCycleId: cycle.id})">
            <a href="#">Сдать</a>
        </div>
        <div class="download">
            <a href="#">Скачать условия</a>
        </div>
    </div>
</template>

<script>
export default {
    name: "CycleLink",
    props: ["cycle"],
    methods: {
        changePage: function (page, kwargs = undefined) {
            this.$root.$emit("onChangePage", page, kwargs);
        },
    },
}
</script>

<style scoped>
.task-cycle-link {
    margin-bottom: 0.5rem;
    margin-left: 1rem;
    margin-right: 1rem;
    text-align: left;
    overflow: auto;
    border: 1px solid var(--border-color);
}

.task-cycle-link div {
    height: 100%;
    padding: 1rem 0.5rem 1rem 0.5rem;
}

.task-cycle-link .title, .class-number, .deadline {
    float: left;
}

.task-cycle-link .download, .submit {
    float: right;
}

.task-cycle-link .title {
    width: 30%;
    padding-left: 1rem;
    text-decoration: underline;
    font-weight: bold;
}

.task-cycle-link .submit {
    border-left: 1px solid var(--border-color);
}

.task-cycle-link .submit, .download {
    background: rgba(231, 229, 229, 0.99);
}

.task-cycle-link .submit a, .download a {
    text-decoration: none;
}

.task-cycle-link .submit:hover, .download:hover {
    background: rgb(183, 180, 180);
}
</style>