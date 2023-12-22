<template>
    <article class="task">
        <div class="title">{{ task.title }}</div>
        <div class="information">Темы: кинематика, бросок под углом к горизонту</div>
        <div class="body">{{ task.text }}</div>
        <ul class="attachment">
            <li>Дополнительные материалы</li>
        </ul>
        <div class="footer"></div>
    </article>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Task",
    props: ["task"]
}
</script>

<style scoped>
.task {
    text-align: left;
}

.task .title {
    font-size: 25px;
    color: var(--caption-color);
    font-weight: bold;
}

.task .information {
    font-size: var(--information-font-size);
    color: var(--information-color);
}

.task .body {
    margin-top: 0.5rem;
    border-left: 5px solid var(--border-color);
    padding-left: 1rem;
}

.task .attachment {
    font-size: var(--information-font-size);
    color: var(--information-color);
    padding-left: 1rem;
    margin-bottom: 0.5rem;
}

.task .attachment li {
    padding-left: 0.25rem;
    margin-bottom: 0.25rem;
}

.task .attachment li:last-child {
    margin-bottom: 0;
}

.task .footer {
    border-radius: var(--border-radius);
    overflow: auto;
    padding: 0.4rem 0.75rem;
}
</style>