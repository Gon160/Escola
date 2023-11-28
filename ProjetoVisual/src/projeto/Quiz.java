package projeto;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import projeto.champions.Champions;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

import java.awt.Font;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Random;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Quiz extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private Champions ch;
	private JLabel lblPergunta;
	private JButton btnA, btnB;
	private int Pos = 0;
	private List<Integer> numsList;
	private projeto.champions.quiz.Quiz quizAtual;
	private int Pontos = 0;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Quiz frame = new Quiz();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Quiz() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 230);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lblPergunta = new JLabel(".");
		lblPergunta.setFont(new Font("Tahoma", Font.PLAIN, 20));
		lblPergunta.setBounds(26, 11, 398, 23);
		contentPane.add(lblPergunta);
		
		btnA = new JButton("New button");
		btnA.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				confirmar(btnA.getText());
			}
		});
		btnA.setBounds(26, 45, 398, 39);
		contentPane.add(btnA);
		
		btnB = new JButton("New button");
		btnB.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				confirmar(btnB.getText());
			}
		});
		btnB.setBounds(26, 89, 398, 39);
		contentPane.add(btnB);
	}
	
	public void Ch (Champions ch) {
		this.ch = ch;
		numsList = randomDasPerguntas();
		pergunta(Pos);
	}
	
	public List<Integer> randomDasPerguntas() {
		int perguntas = ch.getQuiz().length;
		List<Integer> numeros = new ArrayList<>();
		for (int i = 0; i < perguntas; i++) {
			numeros.add(i);
		}
		Collections.shuffle(numeros);
		return numeros;
	}
	
	public void pergunta(int posicao) {
		Random aleatorio = new Random(System.currentTimeMillis());
		int resposta = aleatorio.nextInt(2);
		quizAtual = ch.getQuiz()[numsList.get(posicao)];
		lblPergunta.setText(quizAtual.Q);
		
		if (resposta == 0) {
			btnA.setText(quizAtual.Rs[0]);
			btnB.setText(quizAtual.Rs[1]);
		} else {
			btnA.setText(quizAtual.Rs[1]);
			btnB.setText(quizAtual.Rs[0]);
		}
	}
	
	public void confirmar(String opcao) {
		if (opcao.equalsIgnoreCase(quizAtual.R)) {
			Pontos += quizAtual.P;
			JOptionPane.showMessageDialog(null, "Acertaste e ganhaste mais " + quizAtual.P + " pontos tens um total de " + Pontos + ".");
		} else {
			JOptionPane.showMessageDialog(null, "Erraste");
		}
		
		if(ch.getQuiz().length-1 != Pos) {
			Pos += 1;
			pergunta(Pos);
		} else {
			Jogo jframe = new Jogo();
			jframe.setVisible(true);
			
			dispose();
		}

	}
}
