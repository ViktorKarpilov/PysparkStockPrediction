function downloadCSV(csv, filename) {
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    link.setAttribute('download', filename);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
  
  function parseStockDataToCSV() {
    const rows = document.querySelectorAll('#historicalDataTable > tbody > tr');
    let csvContent = 'Date,Open,High,Low,Close,Adj Close,Volume\n';
  
    rows.forEach((row) => {
      const rowData = [];
      row.querySelectorAll('td').forEach((cell) => {
        rowData.push(cell.textContent.trim().replace(',','.'));
      });
  
      if (rowData.length === 7) {
        csvContent += rowData.join(',') + '\n';
      }
    });
  
    return csvContent;
  }
  
  const csvData = parseStockDataToCSV();
  downloadCSV(csvData, 'stock_data.csv');