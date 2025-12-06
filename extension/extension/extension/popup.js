document.addEventListener('DOMContentLoaded', () => {
  // Placeholder impact – replace later with your real data
  document.getElementById('impact').innerText = "Impact: $0 raised → 0 children safe ❤️";

  document.getElementById('manifesto').onclick = () => {
    window.open('https://github.com/LHMisme420/angelhaven-os/blob/main/manifesto.md', '_blank');
  };

  document.getElementById('shelters').onclick = () => {
    const out = document.getElementById('output');
    out.style.display = 'block';
    out.innerHTML = `
      <strong>Key Partners & Shelters</strong><br><br>
      • <a href="https://love146.org" target="_blank">Love146</a><br>
      • <a href="https://www.ecpatusa.org" target="_blank">ECPAT-USA</a><br>
      • <a href="https://www.notforsalecampaign.org" target="_blank">Not For Sale</a><br><br>
      <small>Full list → <a href="https://github.com/LHMisme420/angelhaven-os/tree/main/resources" target="_blank">GitHub/resources</a></small>
    `;
  };

  document.getElementById('playdoh').onclick = () => {
    alert("Playdoh Protocol activated 🌈\nChoose your color to begin the healing journey…\n(Full interactive flow coming soon)");
  };

  document.getElementById('donate').onclick = () => {
    if (window.solana && window.solana.isPhantom) {
      alert("Phantom wallet connected!\nReal donations will work as soon as your Solana program is deployed 🚀");
    } else {
      alert("Please install Phantom wallet");
      window.open("https://phantom.app", "_blank");
    }
  };
});
