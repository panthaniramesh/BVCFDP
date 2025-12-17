<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Marks to Percentage & Grade</title>
    <style>
      :root{--bg:#f4f7fb;--card:#fff;--accent:#2b7aee;--muted:#666}
      *{box-sizing:border-box;font-family:Segoe UI,Roboto,Arial}
      body{background:var(--bg);margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px}
      .card{width:100%;max-width:520px;background:var(--card);padding:20px;border-radius:8px;box-shadow:0 6px 24px rgba(16,24,40,.08)}
      h1{margin:0 0 12px;font-size:20px}
      label{display:block;margin-top:12px;color:var(--muted)}
      input[type=number]{padding:8px 10px;border:1px solid #d6dbe6;border-radius:6px;width:100%;margin-top:6px}
      .row{display:flex;gap:8px;margin-top:12px}
      button{background:var(--accent);color:#fff;border:0;padding:8px 12px;border-radius:6px;cursor:pointer}
      button#reset{background:#6c757d}
      .hidden{display:none}
      .field{margin-top:10px}
      .result{margin-top:16px;padding:12px;border-radius:6px;background:#f1f6ff;border:1px solid #dbe9ff}
    </style>
  </head>
  <body>
    <main class="card">
      <h1>Student Percentage & Grade Calculator</h1>

      <label for="subjects">Number of subjects:</label>
      <input id="subjects" type="number" min="1" value="3">
      <button id="create">Create fields</button>

      <form id="marksForm" class="hidden">
        <div id="fields"></div>
        <div class="row">
          <button type="button" id="calculate">Calculate</button>
          <button type="button" id="reset">Reset</button>
        </div>
      </form>

      <div id="result" class="result hidden"></div>
    </main>

    <script>
      const subjectsInput = document.getElementById('subjects');
      const createBtn = document.getElementById('create');
      const fieldsDiv = document.getElementById('fields');
      const marksForm = document.getElementById('marksForm');
      const calculateBtn = document.getElementById('calculate');
      const resetBtn = document.getElementById('reset');
      const resultDiv = document.getElementById('result');

      function clearFields() {
        fieldsDiv.innerHTML = '';
      }

      function createFields() {
        const n = parseInt(subjectsInput.value, 10);
        if (!n || n < 1) return alert('Enter a valid number of subjects (>=1)');
        clearFields();
        for (let i = 1; i <= n; i++) {
          const wrapper = document.createElement('div');
          wrapper.className = 'field';

          const label = document.createElement('label');
          label.textContent = `Subject ${i} marks (out of 100):`;

          const input = document.createElement('input');
          input.type = 'number';
          input.min = 0;
          input.max = 100;
          input.value = '';
          input.required = true;

          wrapper.appendChild(label);
          wrapper.appendChild(input);
          fieldsDiv.appendChild(wrapper);
        }
        marksForm.classList.remove('hidden');
        resultDiv.classList.add('hidden');
      }

      function percentageAndGrade(totalMarks, subjects) {
        const maxTotal = subjects * 100;
        const percentage = (totalMarks / maxTotal) * 100;
        let grade;
        if (percentage >= 90) grade = 'A+';
        else if (percentage >= 80) grade = 'A';
        else if (percentage >= 70) grade = 'B';
        else if (percentage >= 60) grade = 'C';
        else if (percentage >= 50) grade = 'D';
        else grade = 'F';
        return { percentage: +percentage.toFixed(2), grade };
      }

      function calculate() {
        const inputs = Array.from(fieldsDiv.querySelectorAll('input'));
        if (inputs.length === 0) return alert('Create fields first');
        let total = 0;
        for (const inp of inputs) {
          const v = parseFloat(inp.value);
          if (isNaN(v) || v < 0 || v > 100) return alert('Enter valid marks between 0 and 100 for all subjects');
          total += v;
        }
        const { percentage, grade } = percentageAndGrade(total, inputs.length);
        resultDiv.innerHTML = `<p><strong>Total Marks:</strong> ${total} / ${inputs.length * 100}</p>
          <p><strong>Percentage:</strong> ${percentage}%</p>
          <p><strong>Grade:</strong> ${grade}</p>`;
        resultDiv.classList.remove('hidden');
      }

      createBtn.addEventListener('click', createFields);
      calculateBtn.addEventListener('click', calculate);
      resetBtn.addEventListener('click', () => {
        marksForm.reset();
        clearFields();
        marksForm.classList.add('hidden');
        resultDiv.classList.add('hidden');
      });

      // initial fields
      createFields();
    </script>
  </body>
</html>