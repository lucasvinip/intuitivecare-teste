<template>
  <div class="container">
    <h1>Busca de Operadoras</h1>
    <input
      v-model="search"
      @input="searchOperadoras"
      type="text"
      placeholder="Digite a modalidade da empresa..."
    />

    <div v-if="operadoras.length" class="resultados">
      <div v-for="(op, index) in operadoras" :key="index" class="card">
        <p><strong>Registro ANS:</strong> {{ op.Registro_ANS }}</p>
        <p><strong>CNPJ:</strong> {{ op.CNPJ }}</p>
        <p><strong>Razão Social:</strong> {{ op.Razao_Social }}</p>
        <p><strong>Modalidade:</strong> {{ op.Modalidade }}</p>
        <p><strong>Cidade:</strong> {{ op.Cidade }}</p>
        <p><strong>UF:</strong> {{ op.UF }}</p>
        <p><strong>Representante:</strong> {{ op.Representante }}</p>
      </div>
    </div>
    <div v-else>
      <p>Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      search: '',
      operadoras: [],
    };
  },
  methods: {
    async searchOperadoras() {
      if (this.search.length < 2) {
        this.operadoras = [];
        return;
      }
      try {
        const response = await fetch(`http://127.0.0.1:5001/buscar?modalidade=${this.search}`);
        const data = await response.json();
        this.operadoras = data;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
        this.operadoras = [];
      }
    },
  },
};
</script>

<style>
.container {
  max-width: 800px;
  margin: 30px auto;
  font-family: Arial, sans-serif;
  padding: 20px;
}

input {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.resultados {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.card {
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card p {
  margin: 5px 0;
}
</style>
