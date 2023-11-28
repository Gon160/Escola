package projeto.champions;

import projeto.champions.quiz.Quiz;

public class Kindred extends Champions{

	@Override
	public String getNome() {
		return "Kindred";
	}

	@Override
	public String getP() {
		return "MARCA FAMILIAR\nOs Kindred marcam alvos para Caçar. Concluir uma Caçada fortalece permanentemente as habilidades básicas deles. A cada 4 caçadas concluídas, o Alcance de Ataque também aumenta.";
	}

	@Override
	public String getQ() {
		return "DANÇA DE FLECHAS\nOs Kindred rolam e disparam até três flechas em alvos próximos.";
	}

	@Override
	public String getW() {
		return "FRENESI DO LOBO\nO Lobo se enraivece e ataca inimigos à sua volta. A Ovelha ganha acúmulos passivamente ao se mover e atacar. Quando totalmente carregado, o próximo ataque da Ovelha recupera Vida.";
	}

	@Override
	public String getE() {
		return "PESAR CRESCENTE\nA Ovelha faz um disparo cuidadoso, reduzindo a velocidade de seu alvo. Se a Ovelha atacar o alvo mais duas vezes, seu próximo ataque fará com que o Lobo salte no inimigo, golpeando-o e causando muito dano";
	}

	@Override
	public String getR() {
		return "REFÚGIO DA OVELHA\nA Ovelha concede refúgio contra a morte para todos os seres vivos em uma área. Até que seu efeito acabe, nada pode morrer. No fim de sua duração, as unidades são curadas.";
	}

	@Override
	public String getLore() {
		return "Em Runeterra, o universo fictício onde se passa o League of Legends, existe uma crença difundida sobre a natureza da morte. As pessoas acreditam em uma entidade conhecida como Kindred, uma força que guia as almas para o outro lado após a morte. Essa entidade toma a forma de um Cordeiro suave e um Lobo selvagem.\n"
				+ "O Cordeiro, representando a aceitação pacífica da morte, busca almas que estão prontas para deixar este mundo. Ele oferece conforto e compaixão àqueles que estão prestes a partir. Por outro lado, o Lobo personifica a morte violenta e caótica, perseguindo almas que resistem ao seu destino inevitável.\n"
				+ "A dualidade desses dois seres, embora opostos em sua abordagem, forma o equilíbrio essencial da morte em Runeterra. Juntos, o Cordeiro e o Lobo mantêm a ordem na transição entre a vida e a morte.\n"
				+ "Kindred é invocada em momentos cruciais quando o destino de uma alma está em jogo. Sua presença é tanto um lembrete da inevitabilidade da morte quanto uma força que assegura que cada vida alcance seu fim de acordo com seu próprio caminho.";
	}
	
	/*
	 * Em Runeterra, o universo fictício onde se passa o League of Legends, existe uma crença difundida sobre a natureza da morte. 
	 * As pessoas acreditam em uma entidade conhecida como Kindred, uma força que guia as almas para o outro lado após a morte. 
	 * Essa entidade toma a forma de um Cordeiro suave e um Lobo selvagem.
	 * 
	 * O Cordeiro, representando a aceitação pacífica da morte, busca almas que estão prontas para deixar este mundo. 
	 * Ele oferece conforto e compaixão àqueles que estão prestes a partir. 
	 * Por outro lado, o Lobo personifica a morte violenta e caótica, perseguindo almas que resistem ao seu destino inevitável.
	 * 
	 * A dualidade desses dois seres, embora opostos em sua abordagem, forma o equilíbrio essencial da morte em Runeterra. 
	 * Juntos, o Cordeiro e o Lobo mantêm a ordem na transição entre a vida e a morte.
	 * 
	 * Kindred é invocada em momentos cruciais quando o destino de uma alma está em jogo. 
	 * Sua presença é tanto um lembrete da inevitabilidade da morte quanto uma força que assegura que cada vida alcance seu fim de acordo com seu próprio caminho.
	 */
	
	@Override
	public Quiz[] getQuiz() {
		Quiz[] quizes = new Quiz[4];
		/*
		 * 1. Pergunta: Qual é a função do Cordeiro na dualidade de Kindred em Runeterra?
		 * Caçar almas violentas.
		 * Oferecer conforto às almas prontas para deixar o mundo.
		 * Resposta correta: Oferecer conforto às almas prontas para deixar o mundo.
		 * 
		 * 2. Pergunta: Qual é o papel do Lobo na concepção de Kindred?
		 * Proteger as almas pacíficas.
		 * Perseguir almas que resistem ao destino inevitável.
		 * Resposta correta: Perseguir almas que resistem ao destino inevitável.
		 * 
		 * 3. Pergunta: Como a dualidade de Kindred contribui para a ordem na transição entre a vida e a morte em Runeterra?
		 * Causando caos e destruição.
		 * Mantendo o equilíbrio essencial entre aceitação pacífica e morte violenta.
		 * Resposta correta: Mantendo o equilíbrio essencial entre aceitação pacífica e morte violenta.
		 * 
		 * 4. Pergunta: Em que situações Kindred é invocada?
		 * Sempre que alguém está prestes a morrer.
		 * Em momentos cruciais quando o destino de uma alma está em jogo.
		 * Resposta correta: Em momentos cruciais quando o destino de uma alma está em jogo.
		 */
		
		String[] p1 = {"Caçar almas violentas.", "Oferecer conforto às almas prontas para deixar o mundo."};
		Quiz quiz = new Quiz("Qual é a função do Cordeiro na dualidade de Kindred em Runeterra?", "Oferecer conforto às almas prontas para deixar o mundo.", p1, 5);
		quizes[0] = quiz;
		String[] p2 = {"Proteger as almas pacíficas.", "Perseguir almas que resistem ao destino inevitável."};
		quiz = new Quiz("Pergunta: Qual é o papel do Lobo na concepção de Kindred?", "Perseguir almas que resistem ao destino inevitável.", p2, 5);
		quizes[1] = quiz;
		String[] p3 = {"Causando caos e destruição.", "Mantendo o equilíbrio essencial entre aceitação pacífica e morte violenta."};
		quiz = new Quiz("Como a dualidade de Kindred contribui para a ordem na transição entre a vida e a morte em Runeterra?", "Mantendo o equilíbrio essencial entre aceitação pacífica e morte violenta.", p3, 5);
		quizes[2] = quiz;
		String[] p4 = {"Sempre que alguém está prestes a morrer.", "Em momentos cruciais quando o destino de uma alma está em jogo."};
		quiz = new Quiz("Em que situações Kindred é invocada?", "Em momentos cruciais quando o destino de uma alma está em jogo.", p4, 5);
		quizes[3] = quiz;
		
		return quizes;
	}

}
