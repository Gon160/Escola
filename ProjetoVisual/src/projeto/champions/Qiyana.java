package projeto.champions;

import projeto.champions.quiz.Quiz;

public class Qiyana extends Champions{
	
	@Override
	public String getNome() {
		return "Qiyana";
	}
	
	@Override
	public String getP() {
		return "PRIVILÉGIO DA REALEZA\nO primeiro ataque básico ou habilidade de Qiyana contra cada inimigo causa dano adicional.";
	}
	
	@Override
	public String getQ() {
		return "CÓLERA ELEMENTAL / LÂMINA DE IXTAL\nQiyana brande sua arma, causando dano com um efeito adicional baseado no seu elemento.";
	}
	
	@Override
	public String getW() {
		return "TERRAFORME\nQiyana avança para um local e encanta sua arma com um elemento. Ataques e habilidades causam dano adicional enquanto sua arma estiver encantada.";
	}
	
	@Override
	public String getE() {
		return "AUDÁCIA\nQiyana avança em um inimigo e causa dano.";
	}
	
	@Override
	public String getR() {
		return "SUPREMA DEMONSTRAÇÃO DE TALENTO\nQiyana lança uma onda de choque que detona quaisquer elementos que ela acertar, atordoando e causando dano a inimigos próximos.";
	}
	
	@Override
	public String getLore() {
		return "Qiyana é uma princesa do reino de Ixaocan, uma nação situada na região de Jonia. Ela é herdeira do trono e detentora de um artefato mágico conhecido como a Pedra de Ixaali. Esta pedra lhe concede o poder de controlar e manipular os elementos naturais ao seu redor, como água, terra e fogo.\n"
				+ "No entanto, Qiyana é ambiciosa e não está satisfeita em apenas herdar o trono. Ela busca poder e reconhecimento por suas próprias habilidades. A história de Qiyana a envolve em eventos de conflito e intriga política, enquanto ela luta para afirmar seu lugar como uma líder formidável. Seu estilo de jogo no League of Legends reflete sua personalidade audaciosa, com habilidades que exploram sua capacidade de controlar os elementos em batalha.";
	}
	
	/*
	 * Qiyana é uma princesa do reino de Ixaocan, uma nação situada na região de Jonia. 
	 * Ela é herdeira do trono e detentora de um artefato mágico conhecido como a Pedra de Ixaali. 
	 * Esta pedra lhe concede o poder de controlar e manipular os elementos naturais ao seu redor, como água, terra e fogo.
	 * 
	 * No entanto, Qiyana é ambiciosa e não está satisfeita em apenas herdar o trono. 
	 * Ela busca poder e reconhecimento por suas próprias habilidades. 
	 * A história de Qiyana a envolve em eventos de conflito e intriga política, enquanto ela luta para afirmar seu lugar como uma líder formidável. 
	 * Seu estilo de jogo no League of Legends reflete sua personalidade audaciosa, com habilidades que exploram sua capacidade de controlar os elementos em batalha.
	 */
	
	@Override
	public Quiz[] getQuiz() {
		Quiz[] quizes = new Quiz[4];
		/*
		 * Pergunta 1: Por que Qiyana é ambiciosa e busca poder?
		 * 	Para proteger seu reino e suas tradições.
		 * 	Para ganhar reconhecimento por suas próprias habilidades.
		 * Resposta correta: Para ganhar reconhecimento por suas próprias habilidades.
		 * 
		 * Pergunta 2: Qual é o artefato mágico que Qiyana possui?
		 * 	Pedra de Jonia.
		 * 	Pedra de Ixaali.
		 * Resposta correta: Pedra de Ixaali.
		 * 
		 * Pergunta 3: O que a Pedra de Ixaali concede a Qiyana?
		 * 	Poder para voar.
		 * 	Poder para controlar e manipular os elementos naturais.
		 * Resposta correta: Poder para controlar e manipular os elementos naturais.
		 * 
		 * Pergunta 4: Qual é o objetivo principal de Qiyana na história?
		 * 	Tornar-se uma artista famosa.
		 *  Afirmar seu lugar como uma líder formidável.
		 * Resposta correta: Afirmar seu lugar como uma líder formidável.
		 */
		
		
		String[] p1 = {"Para proteger seu reino e suas tradições.", "Para ganhar reconhecimento por suas próprias habilidades."};
		Quiz quiz = new Quiz("Por que Qiyana é ambiciosa e busca poder?", "Para ganhar reconhecimento por suas próprias habilidades.", p1, 5);
		quizes[0] = quiz;
		String[] p2 = {"Pedra de Jonia.", "Pedra de Ixaali"};
		quiz = new Quiz("Pergunta 2: Qual é o artefato mágico que Qiyana possui?", "Pedra de Ixaali", p2, 5);
		quizes[1] = quiz;
		String[] p3 = {"Poder para voar.", "Poder para controlar e manipular os elementos naturais."};
		quiz = new Quiz("O que a Pedra de Ixaali concede a Qiyana?", "Poder para controlar e manipular os elementos naturais.", p3, 5);
		quizes[2] = quiz;
		String[] p4 = {"Tornar-se uma artista famosa.", "Afirmar seu lugar como uma líder formidável."};
		quiz = new Quiz("Qual é o objetivo principal de Qiyana na história?", "Afirmar seu lugar como uma líder formidável.", p4, 5);
		quizes[3] = quiz;
		
		return quizes;
	}
	
}
