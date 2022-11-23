<script>
    import { step } from '../store.js';
    import Wrapper from './Wrapper.svelte';
</script>

<div>
    <Wrapper>
        <h1>Génération en cours</h1>
        <button on:click={() => $step++}>click</button>
    </Wrapper>
</div>